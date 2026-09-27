# V2R cluster inventory

2026-09-27T06:14:53.459030+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['2', '3', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 314498895872 available bytes; 82.46% used; 112440826 free inodes.

server1 `/home`: 314498895872 available bytes; 82.46% used; 112440826 free inodes.

server1 `/tmp`: 314498895872 available bytes; 82.46% used; 112440826 free inodes.

server1 `/var/tmp`: 314498895872 available bytes; 82.46% used; 112440826 free inodes.

server1 `/mnt/raid5`: 634703011840 available bytes; 97.09% used; 337400013 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 17621356544 available bytes; 99.02% used; 110365004 free inodes.

server2 `/home`: 17621356544 available bytes; 99.02% used; 110365004 free inodes.

server2 `/tmp`: 17621356544 available bytes; 99.02% used; 110365004 free inodes.

server2 `/var/tmp`: 17621356544 available bytes; 99.02% used; 110365004 free inodes.

server2 `/mnt/raid5`: 573617168384 available bytes; 96.04% used; 444876502 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78575714304 available bytes; 95.62% used; 114062893 free inodes.

server3 `/home`: 78575714304 available bytes; 95.62% used; 114062893 free inodes.

server3 `/data`: 1333255557120 available bytes; 81.57% used; 225765554 free inodes.

server3 `/tmp`: 78575714304 available bytes; 95.62% used; 114062893 free inodes.

server3 `/var/tmp`: 78575714304 available bytes; 95.62% used; 114062893 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110998540288 available bytes; 93.81% used; 114372891 free inodes.

server4 `/home`: 110998540288 available bytes; 93.81% used; 114372891 free inodes.

server4 `/data`: 374478532608 available bytes; 94.82% used; 224771175 free inodes.

server4 `/tmp`: 110998540288 available bytes; 93.81% used; 114372891 free inodes.

server4 `/var/tmp`: 110998540288 available bytes; 93.81% used; 114372891 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
