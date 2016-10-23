{-# LANGUAGE TemplateHaskell #-}
module StringMingling(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All
import           Debug.Trace

main :: IO ()
main = interact run

run :: String -> String
run input = trace output output where
    [p, q] = lines input
    output = concat . zipWith (\a b -> a:[b]) p $ q

prop_run = run "\
\abcde\n\
\pqrst\n\
\" == "apbqcrdset"

prop_run1 = run "\
\hacker\n\
\ranker\n\
\" == "hraacnkkeerr"

return []
runTests = $quickCheckAll
