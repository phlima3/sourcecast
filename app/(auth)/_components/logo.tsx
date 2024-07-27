import Image from "next/image";

export const Logo = () => {
  return (
    <Image src="/logo-full.svg" priority alt="Logo" width={200} height={300} />
  );
};
