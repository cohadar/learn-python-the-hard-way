formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ('one', 'two', 'three', 'five')
print formatter % (True, False, "Yomama's", 'arse')
print formatter % (
	"Multiline in Python",
	"almost does not",
	"seem nat'ral",
	"ynowwhatmsayin."
)


