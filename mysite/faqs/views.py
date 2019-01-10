from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, question_id):
	switcher={
		1:"All you need to do is to sign in/sign up from the home page. For sign up process, you need to verify your email address. Once you sign in, select the language you want to learn and select the time slot. Provide your contact number(only once) to complete the registration process. Wiztute executive will contact you to understand your learning requirement in specific and we will allot a tutor accordingly.",
		2:"Tutor charge on hourly basis. They charge as per their qualification and experience.Wiztute does not control the pricing charges by tutors. Once you have a demo with the tutor, you can subscribe the learning session from the tutor by paying as per tutor’s hourly charges. There is a payment tab on dashboard though which you can pay the amount.",
		3:"No, wiztute tutors do not provide any certificate.",
		4:"Yes, the timings are flexible. You can choose to learn at four different time-slots i.e. 8AM-12PM, 12PM-4PM, 4PM-8PM, 8PM-12AM",
		5:"Once you have the demo with the tutor, you can subscribe the learning session as per your requirement. The whole learning will happen on wiztute platform by direct one-to-one interaction with the tutor. Click on “Go Live” tab at the predetermined time to connect to the tutor.",
		6:"Yes, the whole learning process will be online.",
		7:"As of now, you can start learning any spoken language that you want. I.e. Japanese, French, Spanish, etc"
	}
	return HttpResponse(switcher.get(question_id, "Invalid month"))