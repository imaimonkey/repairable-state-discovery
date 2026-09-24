# V2R cluster inventory

2026-09-24T23:16:04.880045+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319023919104 available bytes; 82.20% used; 112480808 free inodes.

server1 `/home`: 319023919104 available bytes; 82.20% used; 112480808 free inodes.

server1 `/tmp`: 319023919104 available bytes; 82.20% used; 112480808 free inodes.

server1 `/var/tmp`: 319023919104 available bytes; 82.20% used; 112480808 free inodes.

server1 `/mnt/raid5`: 415264612352 available bytes; 98.10% used; 337614843 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 23120220160 available bytes; 98.71% used; 110410812 free inodes.

server2 `/home`: 23120220160 available bytes; 98.71% used; 110410812 free inodes.

server2 `/tmp`: 23120220160 available bytes; 98.71% used; 110410812 free inodes.

server2 `/var/tmp`: 23120220160 available bytes; 98.71% used; 110410812 free inodes.

server2 `/mnt/raid5`: 486578782208 available bytes; 96.64% used; 445151666 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84374593536 available bytes; 95.29% used; 114156083 free inodes.

server3 `/home`: 84374593536 available bytes; 95.29% used; 114156083 free inodes.

server3 `/data`: 148527054848 available bytes; 97.95% used; 225801193 free inodes.

server3 `/tmp`: 84374593536 available bytes; 95.29% used; 114156083 free inodes.

server3 `/var/tmp`: 84374593536 available bytes; 95.29% used; 114156083 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105800110080 available bytes; 94.10% used; 114348306 free inodes.

server4 `/home`: 105800110080 available bytes; 94.10% used; 114348306 free inodes.

server4 `/data`: 61579972608 available bytes; 99.15% used; 225167905 free inodes.

server4 `/tmp`: 105800110080 available bytes; 94.10% used; 114348306 free inodes.

server4 `/var/tmp`: 105800110080 available bytes; 94.10% used; 114348306 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
