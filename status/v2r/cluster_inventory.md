# V2R cluster inventory

2026-09-24T02:50:11.300634+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 325385486336 available bytes; 81.85% used; 112498644 free inodes.

server1 `/home`: 325385486336 available bytes; 81.85% used; 112498644 free inodes.

server1 `/tmp`: 325385486336 available bytes; 81.85% used; 112498644 free inodes.

server1 `/var/tmp`: 325385486336 available bytes; 81.85% used; 112498644 free inodes.

server1 `/mnt/raid5`: 561844498432 available bytes; 97.42% used; 337732316 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40874655744 available bytes; 97.72% used; 110431396 free inodes.

server2 `/home`: 40874655744 available bytes; 97.72% used; 110431396 free inodes.

server2 `/tmp`: 40874655744 available bytes; 97.72% used; 110431396 free inodes.

server2 `/var/tmp`: 40874655744 available bytes; 97.72% used; 110431396 free inodes.

server2 `/mnt/raid5`: 528384536576 available bytes; 96.35% used; 445198771 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292520660992 available bytes; 83.68% used; 114205550 free inodes.

server3 `/home`: 292520660992 available bytes; 83.68% used; 114205550 free inodes.

server3 `/data`: 39729229824 available bytes; 99.45% used; 225845942 free inodes.

server3 `/tmp`: 292520660992 available bytes; 83.68% used; 114205550 free inodes.

server3 `/var/tmp`: 292520660992 available bytes; 83.68% used; 114205550 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106002759680 available bytes; 94.08% used; 114349825 free inodes.

server4 `/home`: 106002759680 available bytes; 94.08% used; 114349825 free inodes.

server4 `/data`: 289727504384 available bytes; 96.00% used; 225387099 free inodes.

server4 `/tmp`: 106002759680 available bytes; 94.08% used; 114349825 free inodes.

server4 `/var/tmp`: 106002759680 available bytes; 94.08% used; 114349825 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
