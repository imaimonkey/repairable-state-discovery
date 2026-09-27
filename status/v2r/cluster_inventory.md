# V2R cluster inventory

2026-09-27T14:15:00.684558+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304745746432 available bytes; 83.00% used; 112401345 free inodes.

server1 `/home`: 304745746432 available bytes; 83.00% used; 112401345 free inodes.

server1 `/tmp`: 304745746432 available bytes; 83.00% used; 112401345 free inodes.

server1 `/var/tmp`: 304745746432 available bytes; 83.00% used; 112401345 free inodes.

server1 `/mnt/raid5`: 630251171840 available bytes; 97.11% used; 337424093 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13405511680 available bytes; 99.25% used; 110351806 free inodes.

server2 `/home`: 13405511680 available bytes; 99.25% used; 110351806 free inodes.

server2 `/tmp`: 13405511680 available bytes; 99.25% used; 110351806 free inodes.

server2 `/var/tmp`: 13405511680 available bytes; 99.25% used; 110351806 free inodes.

server2 `/mnt/raid5`: 527243120640 available bytes; 96.36% used; 444722761 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78557945856 available bytes; 95.62% used; 114062765 free inodes.

server3 `/home`: 78557945856 available bytes; 95.62% used; 114062765 free inodes.

server3 `/data`: 1328735670272 available bytes; 81.64% used; 225757023 free inodes.

server3 `/tmp`: 78557945856 available bytes; 95.62% used; 114062765 free inodes.

server3 `/var/tmp`: 78557945856 available bytes; 95.62% used; 114062765 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110994231296 available bytes; 93.81% used; 114372780 free inodes.

server4 `/home`: 110994231296 available bytes; 93.81% used; 114372780 free inodes.

server4 `/data`: 350750261248 available bytes; 95.15% used; 224727393 free inodes.

server4 `/tmp`: 110994231296 available bytes; 93.81% used; 114372780 free inodes.

server4 `/var/tmp`: 110994231296 available bytes; 93.81% used; 114372780 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
