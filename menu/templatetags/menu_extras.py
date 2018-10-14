from collections import defaultdict
from django import template
from menu.models import MenuItem

register = template.Library()


def get_active_menu(current_url):
    query = '''         WITH RECURSIVE
                           get_parents(n) AS (
                           SELECT id
                           FROM menu_menuitem WHERE explicit_url="{0}"
                           UNION
                           SELECT parent_id FROM menu_menuitem, get_parents
                           WHERE menu_menuitem.id=get_parents.n
                           )
                        SELECT mmi1.id, mmi1.parent_id, mmi1.name,
                               mmi1.explicit_url, mmi1.named_url
                        FROM menu_menuitem AS mmi1
                        JOIN menu_menuitem AS mmi2 ON mmi2.id=mmi1.parent_id
                        WHERE mmi2.id IN get_parents
                        '''.format(current_url)
    result = MenuItem.objects.raw(query)
    tree = defaultdict(list)
    root = 0
    for obj in result:
        tree[obj.parent.id].append(obj)
        if not obj.parent.parent_id and not obj.parent in tree[root]:
            tree[root].append(obj.parent)
    tree = {key: sorted(value, key=lambda x: x.name)
            for key, value in tree.items()}
    tree = {key:
            [{'id': obj.id, 'name': obj.name, 'explicit_url': obj.explicit_url,
              'named_url': obj.named_url} for obj in objs]
            for key, objs in tree.items()}
    tree = {'root': root, 'tree': tree}
    return tree


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    active_menu = get_active_menu(current_url)
    context = {
        'menu': {'name': menu_name},
        'active_path': active_menu,
        'current_url': current_url,
    }
    return context
