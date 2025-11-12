def rate_note(note:int) -> str:
   if note < 10:
     return "unsuccessful"
   if 10 <= note < 12:
     return "acceptable"
   if 12 <= note < 14 :
       return "well"
   if 14 <= note < 16:
       return "very well"
   if 16 <= note <= 20:
       return "excellent"
   return "there is no rate"

