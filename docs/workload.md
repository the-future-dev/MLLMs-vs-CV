Monday 26: 4 hours
- thesis index:
analysis of the problem, statement of the first paths to follow, index overview

Tuesday 27: 8 hours

- application infrastructure:
vanilla web `frontend`
basic flask `backend`

- models overview:
summary inside `APIs.md`

- CLIP model
CLIP model inside backend/models/`CLIP`
for --single image-- classification against ImageNet labels.
Comments:
    errore di cuDNN > al momento CLIP esegue su CPU
    in ogni caso lentezza nell'esecuzione abbastanza rilevante - 45 secondi per immagine. Non so se parallelizzando si migliorino le performances
