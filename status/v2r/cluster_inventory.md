# V2R cluster inventory

2026-09-24T13:20:17.871631+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324023930880 available bytes; 81.92% used; 112481545 free inodes.

server1 `/home`: 324023930880 available bytes; 81.92% used; 112481545 free inodes.

server1 `/tmp`: 324023930880 available bytes; 81.92% used; 112481545 free inodes.

server1 `/var/tmp`: 324023930880 available bytes; 81.92% used; 112481545 free inodes.

server1 `/mnt/raid5`: 417048113152 available bytes; 98.09% used; 337676350 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57541038080 available bytes; 96.79% used; 110428837 free inodes.

server2 `/home`: 57541038080 available bytes; 96.79% used; 110428837 free inodes.

server2 `/tmp`: 57541038080 available bytes; 96.79% used; 110428837 free inodes.

server2 `/var/tmp`: 57541038080 available bytes; 96.79% used; 110428837 free inodes.

server2 `/mnt/raid5`: 506931621888 available bytes; 96.50% used; 445170129 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84747722752 available bytes; 95.27% used; 114174485 free inodes.

server3 `/home`: 84747722752 available bytes; 95.27% used; 114174485 free inodes.

server3 `/data`: 161401774080 available bytes; 97.77% used; 225809465 free inodes.

server3 `/tmp`: 84747722752 available bytes; 95.27% used; 114174485 free inodes.

server3 `/var/tmp`: 84747722752 available bytes; 95.27% used; 114174485 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105770135552 available bytes; 94.10% used; 114348748 free inodes.

server4 `/home`: 105770135552 available bytes; 94.10% used; 114348748 free inodes.

server4 `/data`: 90034466816 available bytes; 98.76% used; 225257183 free inodes.

server4 `/tmp`: 105770135552 available bytes; 94.10% used; 114348748 free inodes.

server4 `/var/tmp`: 105770135552 available bytes; 94.10% used; 114348748 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
