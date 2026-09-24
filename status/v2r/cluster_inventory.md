# V2R cluster inventory

2026-09-24T15:06:05.469826+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324047216640 available bytes; 81.92% used; 112481467 free inodes.

server1 `/home`: 324047216640 available bytes; 81.92% used; 112481467 free inodes.

server1 `/tmp`: 324047216640 available bytes; 81.92% used; 112481467 free inodes.

server1 `/var/tmp`: 324047216640 available bytes; 81.92% used; 112481467 free inodes.

server1 `/mnt/raid5`: 416827260928 available bytes; 98.09% used; 337664012 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57422139392 available bytes; 96.80% used; 110427741 free inodes.

server2 `/home`: 57422139392 available bytes; 96.80% used; 110427741 free inodes.

server2 `/tmp`: 57422139392 available bytes; 96.80% used; 110427741 free inodes.

server2 `/var/tmp`: 57422139392 available bytes; 96.80% used; 110427741 free inodes.

server2 `/mnt/raid5`: 503395741696 available bytes; 96.52% used; 445166615 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84870758400 available bytes; 95.26% used; 114183222 free inodes.

server3 `/home`: 84870758400 available bytes; 95.26% used; 114183222 free inodes.

server3 `/data`: 160554803200 available bytes; 97.78% used; 225807438 free inodes.

server3 `/tmp`: 84870758400 available bytes; 95.26% used; 114183222 free inodes.

server3 `/var/tmp`: 84870758400 available bytes; 95.26% used; 114183222 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105719304192 available bytes; 94.10% used; 114348643 free inodes.

server4 `/home`: 105719304192 available bytes; 94.10% used; 114348643 free inodes.

server4 `/data`: 68797022208 available bytes; 99.05% used; 225256971 free inodes.

server4 `/tmp`: 105719304192 available bytes; 94.10% used; 114348643 free inodes.

server4 `/var/tmp`: 105719304192 available bytes; 94.10% used; 114348643 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
