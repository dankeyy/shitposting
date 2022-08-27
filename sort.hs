import Control.Monad
import Data.Array.ST
import Control.Monad.ST


sort xs len =
  forM_ [0..len] $ \i ->
      forM_ [0..len] $ \j ->
        swapIfSmaller xs i j


swapIfSmaller xs i j = do
  iv <- readArray xs i
  jv <- readArray xs j

  when (iv < jv) $ do
    writeArray xs i jv
    writeArray xs j iv


sortedST xs = runST $ do
    let len = length xs - 1
    arr <- newListArray (0, len) xs :: ST s (STUArray s Int Int)

    sort arr len
    poo <- getElems arr
    return poo


main = print $ sortedST [10,9..1]

-- output:
-- [1,2,3,4,5,6,7,8,9,10]
