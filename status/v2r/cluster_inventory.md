# V2R cluster inventory

2026-09-26T06:37:40.830584+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318768570368 available bytes; 82.22% used; 112476272 free inodes.

server1 `/home`: 318768570368 available bytes; 82.22% used; 112476272 free inodes.

server1 `/tmp`: 318768570368 available bytes; 82.22% used; 112476272 free inodes.

server1 `/var/tmp`: 318768570368 available bytes; 82.22% used; 112476272 free inodes.

server1 `/mnt/raid5`: 219348946944 available bytes; 98.99% used; 337539723 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22314455040 available bytes; 98.76% used; 110403835 free inodes.

server2 `/home`: 22314455040 available bytes; 98.76% used; 110403835 free inodes.

server2 `/tmp`: 22314455040 available bytes; 98.76% used; 110403835 free inodes.

server2 `/var/tmp`: 22314455040 available bytes; 98.76% used; 110403835 free inodes.

server2 `/mnt/raid5`: 272819097600 available bytes; 98.11% used; 445029008 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82563989504 available bytes; 95.39% used; 114110888 free inodes.

server3 `/home`: 82563989504 available bytes; 95.39% used; 114110888 free inodes.

server3 `/data`: 123992141824 available bytes; 98.29% used; 225822148 free inodes.

server3 `/tmp`: 82563989504 available bytes; 95.39% used; 114110888 free inodes.

server3 `/var/tmp`: 82563989504 available bytes; 95.39% used; 114110888 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106076057600 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106076057600 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 106041626624 available bytes; 98.53% used; 224923331 free inodes.

server4 `/tmp`: 106076057600 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106076057600 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
