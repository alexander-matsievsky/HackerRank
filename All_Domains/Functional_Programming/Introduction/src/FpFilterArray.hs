{-# LANGUAGE TemplateHaskell #-}
module FpFilterArray(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    x:bs = map (read::String -> Integer) . lines $ input
    output = unlines . map show . filter (< x) $ bs

prop_run = run "3\n\
\10\n\
\9\n\
\8\n\
\2\n\
\7\n\
\5\n\
\1\n\
\3\n\
\0\n" == "2\n\
\1\n\
\0\n"

return []
runTests = $quickCheckAll
