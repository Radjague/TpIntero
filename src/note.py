def rate_note(note:int) -> str:
   if note < 10:
     return "unsuccessful"
   if note == 11:
     return "acceptable"
   if note == 10:
     return "acceptable"
   return "well"
