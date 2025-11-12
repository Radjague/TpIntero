def rate_note(note:int) -> str:
   if note < 10:
     return "unsuccessful"
   if 10 <= note < 12:
     return "acceptable"
   if 12 <= note < 14 :
       return "well"
   if note == 14:
       return "very well"
   if note == 15:
       return "very well"
   return "excellent"

