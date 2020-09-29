# Simple-Assembler-in-Python
This is a simple 2 pass assembler code written in Python

## Algorithm
1. Read starting address from file and store it in a variable
2. Write address, check mnemonic + register opcode and write them accordingly(hardcode mo &amp; ro and check)
3. if STOP in statement &gt; write string &amp; address
4. if flag==1 &gt; decrement address, update address as per ORIGIN
5. if ele of SYMBOL in line &gt; update symtab, address, value and length accordingly
6. if “=” equals words[0] &gt; update literal table
7. if “=” ! in words &amp; if lit count != 0 &gt; update pool table
8. increment address
9. if ! END goto step 2 else close all files
10.Open all closed files in read mode and create pass2 file
11. In loop of file2 &gt; if Address in words &gt; continue
12. In loop of file1 &gt; if words1[-1] == words2[-1] &gt; write(words1[0]+words2[0]+words1[-1]) &gt; flag=1
13. if flag==0 &gt; write(words1[0]+_________+words1[-1])
14. Similarly check lit table with file1 &amp; write to pass2
15. goto 11 until loop ends
16. Close all files
