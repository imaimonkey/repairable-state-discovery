# V2R cluster inventory

2026-09-27T14:05:51.617743+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304750915584 available bytes; 83.00% used; 112401360 free inodes.

server1 `/home`: 304750915584 available bytes; 83.00% used; 112401360 free inodes.

server1 `/tmp`: 304750915584 available bytes; 83.00% used; 112401360 free inodes.

server1 `/var/tmp`: 304750915584 available bytes; 83.00% used; 112401360 free inodes.

server1 `/mnt/raid5`: 634882748416 available bytes; 97.09% used; 337424238 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 13408591872 available bytes; 99.25% used; 110351813 free inodes.

server2 `/home`: 13408591872 available bytes; 99.25% used; 110351813 free inodes.

server2 `/tmp`: 13408591872 available bytes; 99.25% used; 110351813 free inodes.

server2 `/var/tmp`: 13408591872 available bytes; 99.25% used; 110351813 free inodes.

server2 `/mnt/raid5`: 527503392768 available bytes; 96.36% used; 444723276 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78560043008 available bytes; 95.62% used; 114062773 free inodes.

server3 `/home`: 78560043008 available bytes; 95.62% used; 114062773 free inodes.

server3 `/data`: 1330869649408 available bytes; 81.61% used; 225757174 free inodes.

server3 `/tmp`: 78560043008 available bytes; 95.62% used; 114062773 free inodes.

server3 `/var/tmp`: 78560043008 available bytes; 95.62% used; 114062773 free inodes.
| server4 | True | ['0', '3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110996901888 available bytes; 93.81% used; 114372787 free inodes.

server4 `/home`: 110996901888 available bytes; 93.81% used; 114372787 free inodes.

server4 `/data`: 350786957312 available bytes; 95.15% used; 224727432 free inodes.

server4 `/tmp`: 110996901888 available bytes; 93.81% used; 114372787 free inodes.

server4 `/var/tmp`: 110996901888 available bytes; 93.81% used; 114372787 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
