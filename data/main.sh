main() {
    for i in {0..100}; do
        cp "./nonsense.txt" "./nonsense_${i}.txt"
    done
}

main
