# V2R cluster inventory

2026-09-24T14:58:21.252911+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324045234176 available bytes; 81.92% used; 112481467 free inodes.

server1 `/home`: 324045234176 available bytes; 81.92% used; 112481467 free inodes.

server1 `/tmp`: 324045234176 available bytes; 81.92% used; 112481467 free inodes.

server1 `/var/tmp`: 324045234176 available bytes; 81.92% used; 112481467 free inodes.

server1 `/mnt/raid5`: 416838557696 available bytes; 98.09% used; 337664915 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57429102592 available bytes; 96.80% used; 110427823 free inodes.

server2 `/home`: 57429102592 available bytes; 96.80% used; 110427823 free inodes.

server2 `/tmp`: 57429102592 available bytes; 96.80% used; 110427823 free inodes.

server2 `/var/tmp`: 57429102592 available bytes; 96.80% used; 110427823 free inodes.

server2 `/mnt/raid5`: 503112839168 available bytes; 96.52% used; 445166972 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84855373824 available bytes; 95.26% used; 114183690 free inodes.

server3 `/home`: 84855373824 available bytes; 95.26% used; 114183690 free inodes.

server3 `/data`: 160618070016 available bytes; 97.78% used; 225807587 free inodes.

server3 `/tmp`: 84855373824 available bytes; 95.26% used; 114183690 free inodes.

server3 `/var/tmp`: 84855373824 available bytes; 95.26% used; 114183690 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105719660544 available bytes; 94.10% used; 114348664 free inodes.

server4 `/home`: 105719660544 available bytes; 94.10% used; 114348664 free inodes.

server4 `/data`: 69133357056 available bytes; 99.04% used; 225256976 free inodes.

server4 `/tmp`: 105719660544 available bytes; 94.10% used; 114348664 free inodes.

server4 `/var/tmp`: 105719660544 available bytes; 94.10% used; 114348664 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
