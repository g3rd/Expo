from __future__ import unicode_literals, print_function
from django.contrib.auth.decorators import permission_required
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from slides.models import State, Presentation, Slide


def list(request):
    pass


def _slides(presentation, state):
    return Slide.objects.filter(presentation=presentation, depth__in=[2, 3], visible_states__in=[state]).order_by('path')

def _vote_slides(presentation):
    return Slide.objects.filter(presentation=presentation, depth__gt=1, visible_states__in=State.objects.filter(name='voting')).order_by('path')

def _voting_data(vote_slides):
    voting_data = {
        "name": "root",
        "children": []
    }
    for slide in vote_slides.filter(depth=2):
        voting_data['children'].append(slide.to_jsonable_python_object())
    return JsonResponse(voting_data, safe=False).content

@xframe_options_exempt
def present(request, slug):
    print("PRESENT")
    try:
        presentation = Presentation.published.get(slug=slug)
    except Presentation.DoesNotExist:
        raise Http404

    if request.user.has_perm('slides.change_presentation'):
        state = request.GET.get('state', presentation.state.pk)
    else:
        state = presentation.state

    slides = _slides(presentation, state)

    vote_slides = _vote_slides(presentation)

    context = {
        "presentation": presentation,
        'slides': slides,
        'vote_slides': vote_slides,
        'voting_data': _voting_data(vote_slides),
    }

    return render(request, presentation.template_path, context)


@permission_required('slides.change_presentation')
@xframe_options_exempt
def present_draft(request, slug):
    print("DRAFT")
    try:
        presentation = Presentation.draft.get(slug=slug)
    except Presentation.DoesNotExist:
        raise Http404

    state = request.GET.get('state', presentation.state.pk)
    slides = _slides(presentation, state)
    vote_slides = _vote_slides(presentation)

    context = {
        "presentation": presentation,
        'slides': slides,
        'vote_slides': vote_slides,
        'voting_data': _voting_data(vote_slides),
    }

    return render(request, presentation.template_path, context)
