import subprocess
import sys
from pathlib import Path


def main() -> None:
    proto_dir = Path("src/proto")
    out_dir = Path("src/generated")
    out_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        sys.executable,
        "-m",
        "grpc_tools.protoc",
        f"-I{proto_dir}",
        f"--python_betterproto_out={out_dir}",
        str(proto_dir / "audit.proto"),
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error compiling proto: {result.stderr}")
        sys.exit(1)
    print("Proto compiled successfully.")


if __name__ == "__main__":
    main()
