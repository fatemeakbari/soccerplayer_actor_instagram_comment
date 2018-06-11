
bin/mallet import-file --input input.txt --output malletfile.mallet
bin/mallet train-classifier --input malletfile.mallet --cross-validation 10   --trainer MaxEnt --trainer NaiveBayes


trainer MaxEnt:
  test presicion(actor) = 0.8471
  test presicion(soccer) = 0.6478
  test recall(actor) = 0.75
  test recall(soccer) = 0.7



trainer NaiveBayes:
  test presicion(actor) = 0.8448
  test presicion(soccer) = 0.6455
  test recall(actor) = 0.76
  test recall(soccer) = 0.7
