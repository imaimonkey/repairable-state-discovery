# V2R cluster inventory

2026-09-26T06:49:53.105561+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318767988736 available bytes; 82.22% used; 112476291 free inodes.

server1 `/home`: 318767988736 available bytes; 82.22% used; 112476291 free inodes.

server1 `/tmp`: 318767988736 available bytes; 82.22% used; 112476291 free inodes.

server1 `/var/tmp`: 318767988736 available bytes; 82.22% used; 112476291 free inodes.

server1 `/mnt/raid5`: 219322142720 available bytes; 98.99% used; 337539625 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22320549888 available bytes; 98.75% used; 110403874 free inodes.

server2 `/home`: 22320549888 available bytes; 98.75% used; 110403874 free inodes.

server2 `/tmp`: 22320549888 available bytes; 98.75% used; 110403874 free inodes.

server2 `/var/tmp`: 22320549888 available bytes; 98.75% used; 110403874 free inodes.

server2 `/mnt/raid5`: 272456187904 available bytes; 98.12% used; 445028400 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82567028736 available bytes; 95.39% used; 114110893 free inodes.

server3 `/home`: 82567028736 available bytes; 95.39% used; 114110893 free inodes.

server3 `/data`: 123990855680 available bytes; 98.29% used; 225821954 free inodes.

server3 `/tmp`: 82567028736 available bytes; 95.39% used; 114110893 free inodes.

server3 `/var/tmp`: 82567028736 available bytes; 95.39% used; 114110893 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106075713536 available bytes; 94.08% used; 114348174 free inodes.

server4 `/home`: 106075713536 available bytes; 94.08% used; 114348174 free inodes.

server4 `/data`: 105905410048 available bytes; 98.54% used; 224923086 free inodes.

server4 `/tmp`: 106075713536 available bytes; 94.08% used; 114348174 free inodes.

server4 `/var/tmp`: 106075713536 available bytes; 94.08% used; 114348174 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
