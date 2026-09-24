# V2R cluster inventory

2026-09-24T08:44:07.254590+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324389666816 available bytes; 81.90% used; 112490316 free inodes.

server1 `/home`: 324389666816 available bytes; 81.90% used; 112490316 free inodes.

server1 `/tmp`: 324389666816 available bytes; 81.90% used; 112490316 free inodes.

server1 `/var/tmp`: 324389666816 available bytes; 81.90% used; 112490316 free inodes.

server1 `/mnt/raid5`: 504950218752 available bytes; 97.68% used; 337718894 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57796907008 available bytes; 96.78% used; 110430960 free inodes.

server2 `/home`: 57796907008 available bytes; 96.78% used; 110430960 free inodes.

server2 `/tmp`: 57796907008 available bytes; 96.78% used; 110430960 free inodes.

server2 `/var/tmp`: 57796907008 available bytes; 96.78% used; 110430960 free inodes.

server2 `/mnt/raid5`: 515706744832 available bytes; 96.44% used; 445178909 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 85900795904 available bytes; 95.21% used; 114200228 free inodes.

server3 `/home`: 85900795904 available bytes; 95.21% used; 114200228 free inodes.

server3 `/data`: 173637378048 available bytes; 97.60% used; 225822268 free inodes.

server3 `/tmp`: 85900795904 available bytes; 95.21% used; 114200228 free inodes.

server3 `/var/tmp`: 85900795904 available bytes; 95.21% used; 114200228 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105768632320 available bytes; 94.10% used; 114349102 free inodes.

server4 `/home`: 105768632320 available bytes; 94.10% used; 114349102 free inodes.

server4 `/data`: 254552453120 available bytes; 96.48% used; 225273474 free inodes.

server4 `/tmp`: 105768632320 available bytes; 94.10% used; 114349102 free inodes.

server4 `/var/tmp`: 105768632320 available bytes; 94.10% used; 114349102 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
