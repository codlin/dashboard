from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):

		#判断安全的http请求方式
		if request.method in permissions.SAFE_METHODS:
			return True

		#否则判断是否同一个user
		return obj.user == request.user