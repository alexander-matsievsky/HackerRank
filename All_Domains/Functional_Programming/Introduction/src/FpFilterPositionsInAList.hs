{-# LANGUAGE TemplateHaskell #-}
module FpFilterPositionsInAList(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    xs = lines input
    output = unlines
        . map snd
        . filter (\(i, _) -> i `mod` 2 == 0)
        . zip [(1::Integer)..]
        $ xs

prop_run = run "2\n\
\5\n\
\3\n\
\4\n\
\6\n\
\7\n\
\9\n\
\8\n" == "5\n\
\4\n\
\7\n\
\8\n"

return []
runTests = $quickCheckAll
