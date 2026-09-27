# V2R cluster inventory

2026-09-27T13:16:58.655798+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304673460224 available bytes; 83.00% used; 112401386 free inodes.

server1 `/home`: 304673460224 available bytes; 83.00% used; 112401386 free inodes.

server1 `/tmp`: 304673460224 available bytes; 83.00% used; 112401386 free inodes.

server1 `/var/tmp`: 304673460224 available bytes; 83.00% used; 112401386 free inodes.

server1 `/mnt/raid5`: 634596741120 available bytes; 97.09% used; 337424234 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13418557440 available bytes; 99.25% used; 110351842 free inodes.

server2 `/home`: 13418557440 available bytes; 99.25% used; 110351842 free inodes.

server2 `/tmp`: 13418557440 available bytes; 99.25% used; 110351842 free inodes.

server2 `/var/tmp`: 13418557440 available bytes; 99.25% used; 110351842 free inodes.

server2 `/mnt/raid5`: 528564252672 available bytes; 96.35% used; 444733501 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 78575906816 available bytes; 95.62% used; 114062838 free inodes.

server3 `/home`: 78575906816 available bytes; 95.62% used; 114062838 free inodes.

server3 `/data`: 1331282968576 available bytes; 81.60% used; 225757660 free inodes.

server3 `/tmp`: 78575906816 available bytes; 95.62% used; 114062838 free inodes.

server3 `/var/tmp`: 78575906816 available bytes; 95.62% used; 114062838 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 111010783232 available bytes; 93.81% used; 114372799 free inodes.

server4 `/home`: 111010783232 available bytes; 93.81% used; 114372799 free inodes.

server4 `/data`: 351495360512 available bytes; 95.14% used; 224727794 free inodes.

server4 `/tmp`: 111010783232 available bytes; 93.81% used; 114372799 free inodes.

server4 `/var/tmp`: 111010783232 available bytes; 93.81% used; 114372799 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
