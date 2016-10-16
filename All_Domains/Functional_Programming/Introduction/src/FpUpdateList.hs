{-# LANGUAGE TemplateHaskell #-}
module FpUpdateList(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    xs = map read . lines $ input
    output = unlines . map (show . abs) $ xs

prop_run = run "2\n\
\-4\n\
\3\n\
\-1\n\
\23\n\
\-4\n\
\-54\n" == "2\n\
\4\n\
\3\n\
\1\n\
\23\n\
\4\n\
\54\n"

return []
runTests = $quickCheckAll
