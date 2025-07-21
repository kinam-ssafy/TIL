# CLI 연습하기

---

홈 디렉토리로 이동하기

Practice 디렉토리 생성하기

Practice 안에 Practice_Folder 디렉토리 생성하기

Practice 디렉토리 안의 디렉토리 및 파일 출력하기

Practice 디렉토리에서 practice_file.txt 생성하기

practice_file.txt 를 copy_practice_file.txt 로 복사하기

copy_practice_file.txt 를 Practice_Folder로 위치를 변경하고, 이 때 이름을 moved_practice_file.txt로 변경하기

Practice 디렉토리의 practice_file.txt 파일 삭제하기

Practice_Folder 디렉토리 삭제하기

---

**작성 코드**


cd ~

mkdir Practice

cd Practice

mkdir Practice_Folder

ls

touch practice_file.txt

cp practice_file.txt copy_practice.txt

mv copy_practice_file.txt /c/Users/SSAFY/Desktop/Practice/Practice_Folder/moved_practice_file.txt

cd ..

rm practice_file.txt

rm -r Practice_Folder

cd ..

rm -r Practice

