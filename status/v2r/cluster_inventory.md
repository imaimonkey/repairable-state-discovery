# V2R cluster inventory

2026-09-27T14:31:47.372881+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304736849920 available bytes; 83.00% used; 112401363 free inodes.

server1 `/home`: 304736849920 available bytes; 83.00% used; 112401363 free inodes.

server1 `/tmp`: 304736849920 available bytes; 83.00% used; 112401363 free inodes.

server1 `/var/tmp`: 304736849920 available bytes; 83.00% used; 112401363 free inodes.

server1 `/mnt/raid5`: 630249463808 available bytes; 97.11% used; 337424058 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13412130816 available bytes; 99.25% used; 110351784 free inodes.

server2 `/home`: 13412130816 available bytes; 99.25% used; 110351784 free inodes.

server2 `/tmp`: 13412130816 available bytes; 99.25% used; 110351784 free inodes.

server2 `/var/tmp`: 13412130816 available bytes; 99.25% used; 110351784 free inodes.

server2 `/mnt/raid5`: 526739890176 available bytes; 96.36% used; 444722144 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78558064640 available bytes; 95.62% used; 114062775 free inodes.

server3 `/home`: 78558064640 available bytes; 95.62% used; 114062775 free inodes.

server3 `/data`: 1328705990656 available bytes; 81.64% used; 225756824 free inodes.

server3 `/tmp`: 78558064640 available bytes; 95.62% used; 114062775 free inodes.

server3 `/var/tmp`: 78558064640 available bytes; 95.62% used; 114062775 free inodes.
| server4 | True | ['0', '1', '3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 109780152320 available bytes; 93.87% used; 114372776 free inodes.

server4 `/home`: 109780152320 available bytes; 93.87% used; 114372776 free inodes.

server4 `/data`: 350476578816 available bytes; 95.16% used; 224727371 free inodes.

server4 `/tmp`: 109780152320 available bytes; 93.87% used; 114372776 free inodes.

server4 `/var/tmp`: 109780152320 available bytes; 93.87% used; 114372776 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
