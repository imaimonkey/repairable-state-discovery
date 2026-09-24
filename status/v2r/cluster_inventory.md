# V2R cluster inventory

2026-09-24T11:47:50.951534+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324341514240 available bytes; 81.91% used; 112488802 free inodes.

server1 `/home`: 324341514240 available bytes; 81.91% used; 112488802 free inodes.

server1 `/tmp`: 324341514240 available bytes; 81.91% used; 112488802 free inodes.

server1 `/var/tmp`: 324341514240 available bytes; 81.91% used; 112488802 free inodes.

server1 `/mnt/raid5`: 424342482944 available bytes; 98.05% used; 337687230 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57642266624 available bytes; 96.78% used; 110429820 free inodes.

server2 `/home`: 57642266624 available bytes; 96.78% used; 110429820 free inodes.

server2 `/tmp`: 57642266624 available bytes; 96.78% used; 110429820 free inodes.

server2 `/var/tmp`: 57642266624 available bytes; 96.78% used; 110429820 free inodes.

server2 `/mnt/raid5`: 510090596352 available bytes; 96.48% used; 445172780 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85244407808 available bytes; 95.24% used; 114166876 free inodes.

server3 `/home`: 85244407808 available bytes; 95.24% used; 114166876 free inodes.

server3 `/data`: 163668738048 available bytes; 97.74% used; 225815915 free inodes.

server3 `/tmp`: 85244407808 available bytes; 95.24% used; 114166876 free inodes.

server3 `/var/tmp`: 85244407808 available bytes; 95.24% used; 114166876 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105727627264 available bytes; 94.10% used; 114348832 free inodes.

server4 `/home`: 105727627264 available bytes; 94.10% used; 114348832 free inodes.

server4 `/data`: 115387281408 available bytes; 98.41% used; 225257951 free inodes.

server4 `/tmp`: 105727627264 available bytes; 94.10% used; 114348832 free inodes.

server4 `/var/tmp`: 105727627264 available bytes; 94.10% used; 114348832 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
