# V2R cluster inventory

2026-09-24T11:08:43.833951+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324376272896 available bytes; 81.90% used; 112488977 free inodes.

server1 `/home`: 324376272896 available bytes; 81.90% used; 112488977 free inodes.

server1 `/tmp`: 324376272896 available bytes; 81.90% used; 112488977 free inodes.

server1 `/var/tmp`: 324376272896 available bytes; 81.90% used; 112488977 free inodes.

server1 `/mnt/raid5`: 476666097664 available bytes; 97.81% used; 337692339 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 57691373568 available bytes; 96.78% used; 110430209 free inodes.

server2 `/home`: 57691373568 available bytes; 96.78% used; 110430209 free inodes.

server2 `/tmp`: 57691373568 available bytes; 96.78% used; 110430209 free inodes.

server2 `/var/tmp`: 57691373568 available bytes; 96.78% used; 110430209 free inodes.

server2 `/mnt/raid5`: 511579099136 available bytes; 96.47% used; 445174069 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 85622411264 available bytes; 95.22% used; 114193736 free inodes.

server3 `/home`: 85622411264 available bytes; 95.22% used; 114193736 free inodes.

server3 `/data`: 163954262016 available bytes; 97.73% used; 225817084 free inodes.

server3 `/tmp`: 85622411264 available bytes; 95.22% used; 114193736 free inodes.

server3 `/var/tmp`: 85622411264 available bytes; 95.22% used; 114193736 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105733554176 available bytes; 94.10% used; 114348921 free inodes.

server4 `/home`: 105733554176 available bytes; 94.10% used; 114348921 free inodes.

server4 `/data`: 115728941056 available bytes; 98.40% used; 225258199 free inodes.

server4 `/tmp`: 105733554176 available bytes; 94.10% used; 114348921 free inodes.

server4 `/var/tmp`: 105733554176 available bytes; 94.10% used; 114348921 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
