from django.shortcuts import render
from dashboard.models import visualize
from django.db.models import Q
from django.db.models import Sum
from django.db.models.functions import Coalesce 


def dash(request):
    qs=visualize.objects.all()
    ut_no = qs.filter(country='United States of America').count()
    ut_no = int(ut_no)
    me_no = qs.filter(country='Mexico').count()
    me_no = int(me_no)
    ru_no = qs.filter(country='Russia').count()
    ru_no = int(ru_no)
    eq_no = qs.filter(country='Egypt').count()
    eq_no = int(eq_no)
    in_no = qs.filter(country='India').count()
    in_no = int(in_no)
    country_list = ['USA', 'Mexico', 'Russia', 'Egypt',"India"]
    number_list = [ut_no,me_no, ru_no, eq_no, in_no]
    
    #if request.method == "POST":
    sd=(request.POST.get( 'start_year'))
    ed=(request.POST.get("end_year"))
    if sd!=""and ed!="" and sd is not None and ed is not None:
     qs=qs.filter(start_year=sd,end_year=ed)
    
    if sd!=""and ed!="" and sd is not None and ed is not None:
     pt1=visualize.objects.filter(published__contains=sd).count()
     pt2=visualize.objects.filter(published__contains=ed).count()
     pt_no=int(pt1)
     pt_no2=int(pt2)
    else:
     pt1=0
     pt2=0
     pt_no=0
     pt_no2=0
       
    published_list=[pt_no, pt_no2]              
    return render(request,"index.html",context={'data':qs,"country_list":country_list,"total":number_list,"st":sd,"ed":ed,"publish":published_list})



def records(request):
   con=visualize.objects.all()
   if request.method=="POST": 
     contr=request.POST.get("contry")
     con=visualize.objects.filter(country=contr)
   fil=int(con.count())
   return render(request,"somerecords.html",context={"record":con,"num":fil})



def register(request):
   if request.method=="POST":
      pass
   return render(request,"register.html")



def login(request):
   if request.method=="POST":
      pass
   return render(request,"login.html")



def topic(request):
   q=visualize.objects.values("topic").distinct()
   s=q.count()
   p=visualize.objects.values("pestle").distinct()
   r=p.count()


   ut_no = q.filter(country='United States of America',topic="gas").count()
   ut_no = int(ut_no)
   me_no = q.filter(country='Mexico',topic="gas").count()
   me_no = int(me_no)
   ir_no = q.filter(country='Iran',topic="gas").count()
   ir_no = int(ir_no)
   ja_no = q.filter(country='Japan',topic="gas").count()
   ja_no = int(ja_no)
   in_no = q.filter(country='India',topic="gas").count()
   in_no = int(in_no)
   eg_no = q.filter(country='Egypt',topic="gas").count()
   eg_no = int(eg_no)
   cont_list = ['USA', 'Mexico', 'Iran', 'Japan',"India","Egypt"]
   numb_list = [ut_no,me_no, ir_no, ja_no, in_no,eg_no]

   ot_no = q.filter(country='United States of America',topic="oil").count()
   ot_no = int(ut_no)
   oe_no = q.filter(country='Mexico',topic="oil").count()
   oe_no = int(me_no)
   ou_no = q.filter(country='Russia',topic="oil").count()
   ou_no = int(ou_no)
   oq_no = q.filter(country='Egypt',topic="oil").count()
   oq_no = int(oq_no)
   on_no = q.filter(country='India',topic="oil").count()
   on_no = int(in_no)
   Un_no = q.filter(country='UAE',topic="oil").count()
   Un_no = int(Un_no)
   conta_list = ['USA', 'Mexico', 'Russia', 'Egypt',"India","UAE"]
   numbo_list = [ot_no, oe_no, ou_no, oq_no, on_no,Un_no]

   x=q=visualize.objects.values("topic").distinct()[0:10]
   a=q=visualize.objects.values("topic").distinct()[10:20]
   b=q=visualize.objects.values("topic").distinct()[20:30]
   c=q=visualize.objects.values("topic").distinct()[30:40]
   d=q=visualize.objects.values("topic").distinct()[40:50]
   e=q=visualize.objects.values("topic").distinct()[50:60]
   f=q=visualize.objects.values("topic").distinct()[60:70]
   g=q=visualize.objects.values("topic").distinct()[70:80]
   h=q=visualize.objects.values("topic").distinct()[80:90]
   y=q=visualize.objects.values("topic").distinct()[90:99]

   
       
   return render (request,"topic.html",{"top":q,"country_list":cont_list,"totalgas":numb_list,"totaloil":numbo_list,"t":s,"pest":p,"r":r,"countr":conta_list,"topic1":x,"topic2":a,"topic3":b,"topic4":c,"topic5":d,"topic6":e,"topic7":f,"topic8":g,"topic9":h,"topic10":y})
   
def home(request):
   qs=visualize.objects.all()
   ut_no = qs.filter(country='United States of America').count()
   ut_no = int(ut_no)
   me_no = qs.filter(country='Mexico').count()
   me_no = int(me_no)
   ru_no = qs.filter(country='Russia').count()
   ru_no = int(ru_no)
   eq_no = qs.filter(country='Egypt').count()
   eq_no = int(eq_no)
   in_no = qs.filter(country='India').count()
   in_no = int(in_no)
   country_list = ['USA', 'Mexico', 'Russia', 'Egypt',"India"]
   number_list = [ut_no,me_no, ru_no, eq_no, in_no]

   iu=visualize.objects.filter(country='United States of America').aggregate(intensity_sum=Coalesce(Sum("intensity"), 0))
   im=visualize.objects.filter(country='Mexico').aggregate(intensity_sum=Coalesce(Sum("intensity"), 0))
   ir=visualize.objects.filter(country="Russia").aggregate(intensity_sum=Coalesce(Sum("intensity"), 0))
   ie=visualize.objects.filter(country='Egypt').aggregate(intensity_sum=Coalesce(Sum("intensity"), 0))
   ii=visualize.objects.filter(country='India').aggregate(intensity_sum=Coalesce(Sum("intensity"), 0))
   intensity=[iu["intensity_sum"],im["intensity_sum"],ir["intensity_sum"],ie["intensity_sum"],ii["intensity_sum"]]

   ru=visualize.objects.filter(country='United States of America').aggregate(reference_sum=Coalesce(Sum("relevance"), 0))
   rm=visualize.objects.filter(country='Mexico').aggregate(reference_sum=Coalesce(Sum("relevance"), 0))
   rr=visualize.objects.filter(country="Russia").aggregate(reference_sum=Coalesce(Sum("relevance"), 0))
   re=visualize.objects.filter(country='Egypt').aggregate(reference_sum=Coalesce(Sum("relevance"), 0))
   ri=visualize.objects.filter(country='India').aggregate(reference_sum=Coalesce(Sum("relevance"), 0))
   reference=[ru["reference_sum"],rm["reference_sum"],rr["reference_sum"],re["reference_sum"],ri["reference_sum"]]

   npb=visualize.objects.filter(published="").count()
   npb=int(npb)
   pb=visualize.objects.filter(~Q(published ="")).count()
   pb=int(pb)
   publish_list=["Published Topic","UnPublished Topic"]
   pub=[pb,npb]

   ol_no = qs.filter(topic='oil').count()
   ol_no = int(ol_no)
   gs_no = qs.filter(topic='gas').count()
   gs_no = int(gs_no)
   co_no = qs.filter(topic='consumption').count()
   co_no = int(co_no)
   bi_no = qs.filter(topic='biofuel').count()
   bi_no = int(bi_no)
   ec_no = qs.filter(topic='economy').count()
   ec_no = int(ec_no)
   wa_no = qs.filter(topic='war').count()
   wa_no = int(wa_no)
   ba_no = qs.filter(topic='battery').count()
   ba_no = int(ba_no)
   cl_no = qs.filter(topic='climate').count()
   cl_no = int(cl_no)
   en_no = qs.filter(topic='energy').count()
   en_no = int(en_no)
   cr_no = qs.filter(topic='crisis').count()
   cr_no = int(cr_no)
   ic_no = qs.filter(topic='ice').count()
   ic_no = int(ic_no)
   ca_no = qs.filter(topic='car').count()
   ca_no = int(ca_no)
   ba_no = qs.filter(topic='bank').count()
   ba_no = int(ba_no)
   
   topic_list = ['Oil', 'Gas', 'Consumption', 'Biofuel',"Economy","War","Battery","Climate","Energy","Crisis","Ice","Car","Bank"]
   value_list = [ol_no,gs_no, co_no, bi_no, ec_no,wa_no,ba_no,cl_no,en_no,cr_no,ic_no,ca_no,ba_no]

   return render(request,"dash.html",context={"cont_list":country_list,"totalint":intensity,"totalref":reference,"publishlist":publish_list,"pub":pub,"number":number_list,"topic":topic_list,"values":value_list})
