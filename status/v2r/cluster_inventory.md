# V2R cluster inventory

2026-09-26T06:46:50.038915+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318768488448 available bytes; 82.22% used; 112476291 free inodes.

server1 `/home`: 318768488448 available bytes; 82.22% used; 112476291 free inodes.

server1 `/tmp`: 318768488448 available bytes; 82.22% used; 112476291 free inodes.

server1 `/var/tmp`: 318768488448 available bytes; 82.22% used; 112476291 free inodes.

server1 `/mnt/raid5`: 219324297216 available bytes; 98.99% used; 337539631 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22321348608 available bytes; 98.75% used; 110403879 free inodes.

server2 `/home`: 22321348608 available bytes; 98.75% used; 110403879 free inodes.

server2 `/tmp`: 22321348608 available bytes; 98.75% used; 110403879 free inodes.

server2 `/var/tmp`: 22321348608 available bytes; 98.75% used; 110403879 free inodes.

server2 `/mnt/raid5`: 272545472512 available bytes; 98.12% used; 445028468 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82566938624 available bytes; 95.39% used; 114110892 free inodes.

server3 `/home`: 82566938624 available bytes; 95.39% used; 114110892 free inodes.

server3 `/data`: 123992260608 available bytes; 98.29% used; 225821991 free inodes.

server3 `/tmp`: 82566938624 available bytes; 95.39% used; 114110892 free inodes.

server3 `/var/tmp`: 82566938624 available bytes; 95.39% used; 114110892 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106075791360 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106075791360 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105906475008 available bytes; 98.54% used; 224923191 free inodes.

server4 `/tmp`: 106075791360 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106075791360 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
