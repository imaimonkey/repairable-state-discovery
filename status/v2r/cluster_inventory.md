# V2R cluster inventory

2026-09-27T14:11:57.716924+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304746946560 available bytes; 83.00% used; 112401343 free inodes.

server1 `/home`: 304746946560 available bytes; 83.00% used; 112401343 free inodes.

server1 `/tmp`: 304746946560 available bytes; 83.00% used; 112401343 free inodes.

server1 `/var/tmp`: 304746946560 available bytes; 83.00% used; 112401343 free inodes.

server1 `/mnt/raid5`: 630252498944 available bytes; 97.11% used; 337424096 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 13406015488 available bytes; 99.25% used; 110351806 free inodes.

server2 `/home`: 13406015488 available bytes; 99.25% used; 110351806 free inodes.

server2 `/tmp`: 13406015488 available bytes; 99.25% used; 110351806 free inodes.

server2 `/var/tmp`: 13406015488 available bytes; 99.25% used; 110351806 free inodes.

server2 `/mnt/raid5`: 526790893568 available bytes; 96.36% used; 444722823 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 78558670848 available bytes; 95.62% used; 114062769 free inodes.

server3 `/home`: 78558670848 available bytes; 95.62% used; 114062769 free inodes.

server3 `/data`: 1328805425152 available bytes; 81.64% used; 225757064 free inodes.

server3 `/tmp`: 78558670848 available bytes; 95.62% used; 114062769 free inodes.

server3 `/var/tmp`: 78558670848 available bytes; 95.62% used; 114062769 free inodes.
| server4 | True | ['3', '5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 110996738048 available bytes; 93.81% used; 114372787 free inodes.

server4 `/home`: 110996738048 available bytes; 93.81% used; 114372787 free inodes.

server4 `/data`: 350750076928 available bytes; 95.15% used; 224727391 free inodes.

server4 `/tmp`: 110996738048 available bytes; 93.81% used; 114372787 free inodes.

server4 `/var/tmp`: 110996738048 available bytes; 93.81% used; 114372787 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
