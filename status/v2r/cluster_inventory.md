# V2R cluster inventory

2026-09-26T01:58:15.831080+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318526509056 available bytes; 82.23% used; 112476292 free inodes.

server1 `/home`: 318526509056 available bytes; 82.23% used; 112476292 free inodes.

server1 `/tmp`: 318526509056 available bytes; 82.23% used; 112476292 free inodes.

server1 `/var/tmp`: 318526509056 available bytes; 82.23% used; 112476292 free inodes.

server1 `/mnt/raid5`: 345235791872 available bytes; 98.42% used; 337546322 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22928629760 available bytes; 98.72% used; 110406216 free inodes.

server2 `/home`: 22928629760 available bytes; 98.72% used; 110406216 free inodes.

server2 `/tmp`: 22928629760 available bytes; 98.72% used; 110406216 free inodes.

server2 `/var/tmp`: 22928629760 available bytes; 98.72% used; 110406216 free inodes.

server2 `/mnt/raid5`: 289901166592 available bytes; 98.00% used; 445055032 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84326023168 available bytes; 95.29% used; 114152370 free inodes.

server3 `/home`: 84326023168 available bytes; 95.29% used; 114152370 free inodes.

server3 `/data`: 124791840768 available bytes; 98.28% used; 225817552 free inodes.

server3 `/tmp`: 84326023168 available bytes; 95.29% used; 114152370 free inodes.

server3 `/var/tmp`: 84326023168 available bytes; 95.29% used; 114152370 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105433825280 available bytes; 94.12% used; 114348357 free inodes.

server4 `/home`: 105433825280 available bytes; 94.12% used; 114348357 free inodes.

server4 `/data`: 130906103808 available bytes; 98.19% used; 224915774 free inodes.

server4 `/tmp`: 105433825280 available bytes; 94.12% used; 114348357 free inodes.

server4 `/var/tmp`: 105433825280 available bytes; 94.12% used; 114348357 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
