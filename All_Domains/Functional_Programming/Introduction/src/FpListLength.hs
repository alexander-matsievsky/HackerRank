{-# LANGUAGE TemplateHaskell #-}
module FpListLength(runTests) where
import           Test.QuickCheck
import           Test.QuickCheck.All

main :: IO ()
main = interact run

run :: String -> String
run input = output where
    xs = lines input
    output = show . len $ xs

len :: [t] -> Int
len = foldr (\_ l -> l + 1) 0

prop_run = run "2\n\
\5\n\
\1\n\
\4\n\
\3\n\
\7\n\
\8\n\
\6\n\
\0\n\
\9\n" == "10"

prop_run1 xs = len xs == length xs

return []
runTests = $quickCheckAll
