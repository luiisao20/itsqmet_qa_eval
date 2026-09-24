from django.shortcuts import render, get_object_or_404, redirect

from .models import Contact
from .forms import ContactForm
# Create your views here.

def contacts_list(request):
  contacts = Contact.objects.all()
  return render(request, "contacts/contacts_list.html", {"contacts": contacts})

def contact_detail(request, id):
  contact = get_object_or_404(Contact, id=id)
  return render(request, "contacts/contact_detail.html", {"contact": contact})

def contact_create(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      form.save()
      return render(request, "contacts/contact_detail.html", {"contact": form.instance})
  else:
    form = ContactForm()
  return render(request, "contacts/contact_form.html", {'form': form})

def contact_update(request, id):
  contact = get_object_or_404(Contact, id=id)

  if request.method == 'POST':
    form = ContactForm(request.POST, instance=contact)
    if form.is_valid():
      form.save()
      return render(request, "contacts/contact_detail.html", {"contact": form.instance})
  else:
    form = ContactForm(instance=contact)
  return render(request, "contacts/contact_form.html", {'form': form})

def contact_delete(request, id):
  contact = get_object_or_404(Contact, id=id)
  contact.delete()
  return redirect("contacts_list")