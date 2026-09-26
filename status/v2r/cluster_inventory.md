# V2R cluster inventory

2026-09-26T11:33:43.105423+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318198521856 available bytes; 82.25% used; 112474809 free inodes.

server1 `/home`: 318198521856 available bytes; 82.25% used; 112474809 free inodes.

server1 `/tmp`: 318198521856 available bytes; 82.25% used; 112474809 free inodes.

server1 `/var/tmp`: 318198521856 available bytes; 82.25% used; 112474809 free inodes.

server1 `/mnt/raid5`: 218686513152 available bytes; 99.00% used; 337538055 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 19792441344 available bytes; 98.90% used; 110383621 free inodes.

server2 `/home`: 19792441344 available bytes; 98.90% used; 110383621 free inodes.

server2 `/tmp`: 19792441344 available bytes; 98.90% used; 110383621 free inodes.

server2 `/var/tmp`: 19792441344 available bytes; 98.90% used; 110383621 free inodes.

server2 `/mnt/raid5`: 241315930112 available bytes; 98.33% used; 444978125 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82650222592 available bytes; 95.39% used; 114110825 free inodes.

server3 `/home`: 82650222592 available bytes; 95.39% used; 114110825 free inodes.

server3 `/data`: 123442999296 available bytes; 98.29% used; 225825471 free inodes.

server3 `/tmp`: 82650222592 available bytes; 95.39% used; 114110825 free inodes.

server3 `/var/tmp`: 82650222592 available bytes; 95.39% used; 114110825 free inodes.
| server4 | True | ['0', '3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105909497856 available bytes; 94.09% used; 114347936 free inodes.

server4 `/home`: 105909497856 available bytes; 94.09% used; 114347936 free inodes.

server4 `/data`: 88636563456 available bytes; 98.78% used; 224879407 free inodes.

server4 `/tmp`: 105909497856 available bytes; 94.09% used; 114347936 free inodes.

server4 `/var/tmp`: 105909497856 available bytes; 94.09% used; 114347936 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
