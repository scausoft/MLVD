
def initial_session(user, request):
    permissions = user.roles.all().values("permissions__url").distinct()  # .distinct()去重

    permission_list = []

    for item in permissions:
        permission_list.append(item["permissions__url"])
    print(permission_list)

    request.session["permission_list"] = permission_list
