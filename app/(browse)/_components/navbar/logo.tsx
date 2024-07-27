import Image from "next/image";
import Link from "next/link";

export const Logo = () => {
  return (
    <Link href="/" passHref>
      <div className="flex  items-center gap-x-4 hover:opacity-75 transition">
        <Image
          src="/logo-draw.svg"
          priority
          className="mr-12 shrink-0 lg:mr-0 lg:shrink"
          alt="Logo"
          width={32}
          height={32}
        />
      </div>
    </Link>
  );
};
