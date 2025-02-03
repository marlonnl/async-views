from django.http import HttpResponse


def index(request):
	return HttpResponse(
		"""
		Async e sync views com Django.
		<br>
		<ul>
			<li><a href='/async/'>async</a></li>
			<li><a href='/sync/'>sync</a></li>
		</ul>
		""" 
	)