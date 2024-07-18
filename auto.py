import os
import subprocess
import shutil
import tempfile
import sys
print(os.system('apt list cv2'))

# 설정
GIT_REPO_URL = "https://github.com/username/repo-name.git"
PACKAGE_DIR = "/packages"

def run_command(command, cwd=None):
    result = subprocess.run(command, shell=True, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        print(f"stdout: {result.stdout.decode()}")
        print(f"stderr: {result.stderr.decode()}")
        raise RuntimeError(f"Command failed: {command}")
    return result.stdout.decode()

def main():
    # 작업 디렉토리 생성
    work_dir = tempfile.mkdtemp()
    try:
        # Git 리포지토리 클론
        print("Cloning repository...")
        run_command(f"git clone {GIT_REPO_URL} .", cwd=work_dir)

        # 패키지 빌드
        # print("Building package...")
        # run_command(f"cp /root/setup.py {work_dir}", cwd="/root")
        # run_command("python setup.py sdist bdist_wheel", cwd=work_dir)

        # 빌드된 패키지 파일 경로
        dist_dir = os.path.join(work_dir, "dist")
        if not os.path.exists(dist_dir):
            raise RuntimeError(f"Dist directory not found: {dist_dir}")

        # 패키지 업로드
        print("Copying packages to pypiserver...")
        for filename in os.listdir(dist_dir):
            full_file_name = os.path.join(dist_dir, filename)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, PACKAGE_DIR)

        print("Package update complete.")
    finally:
        # 임시 작업 디렉토리 삭제
        shutil.rmtree(work_dir)

if __name__ == "__main__":
    main()
