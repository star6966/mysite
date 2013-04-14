from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from polls.models import Poll, Choice

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "YOU DUN DID DAT WRONG!.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

