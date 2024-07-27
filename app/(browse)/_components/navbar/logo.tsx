import Image from "next/image";
import Link from "next/link";

export const Logo = () => {
  return (
    <Link href="/" passHref>
      <div className="hidden lg:flex items-center gap-x-4 hover:opacity-75 transition">
        <Image
          src="/logo-draw.svg"
          priority
          alt="Logo"
          width={32}
          height={32}
        />
      </div>
    </Link>
  );
};
