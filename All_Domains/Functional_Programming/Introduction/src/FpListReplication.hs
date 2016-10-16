{-# LANGUAGE TemplateHaskell #-}
module FpListReplication(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    s:xs = lines input
    output = unlines . concatMap (replicate (read s)) $ xs

prop_run = run "3\n\
\1\n\
\2\n\
\3\n\
\4\n" == "1\n\
\1\n\
\1\n\
\2\n\
\2\n\
\2\n\
\3\n\
\3\n\
\3\n\
\4\n\
\4\n\
\4\n"

return []
runTests = $quickCheckAll
