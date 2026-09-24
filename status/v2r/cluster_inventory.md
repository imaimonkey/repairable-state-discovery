# V2R cluster inventory

2026-09-24T15:37:04.736974+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324020011008 available bytes; 81.92% used; 112481438 free inodes.

server1 `/home`: 324020011008 available bytes; 81.92% used; 112481438 free inodes.

server1 `/tmp`: 324020011008 available bytes; 81.92% used; 112481438 free inodes.

server1 `/var/tmp`: 324020011008 available bytes; 81.92% used; 112481438 free inodes.

server1 `/mnt/raid5`: 416740458496 available bytes; 98.09% used; 337660359 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 57386029056 available bytes; 96.80% used; 110427431 free inodes.

server2 `/home`: 57386029056 available bytes; 96.80% used; 110427431 free inodes.

server2 `/tmp`: 57386029056 available bytes; 96.80% used; 110427431 free inodes.

server2 `/var/tmp`: 57386029056 available bytes; 96.80% used; 110427431 free inodes.

server2 `/mnt/raid5`: 502570606592 available bytes; 96.53% used; 445165781 free inodes.
| server3 | True | ['0'] | [] | reference_compatible=True |

server3 `/`: 84473528320 available bytes; 95.29% used; 114157052 free inodes.

server3 `/home`: 84473528320 available bytes; 95.29% used; 114157052 free inodes.

server3 `/data`: 160314290176 available bytes; 97.78% used; 225806422 free inodes.

server3 `/tmp`: 84473528320 available bytes; 95.29% used; 114157052 free inodes.

server3 `/var/tmp`: 84473528320 available bytes; 95.29% used; 114157052 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105715957760 available bytes; 94.10% used; 114348618 free inodes.

server4 `/home`: 105715957760 available bytes; 94.10% used; 114348618 free inodes.

server4 `/data`: 89395273728 available bytes; 98.76% used; 225256700 free inodes.

server4 `/tmp`: 105715957760 available bytes; 94.10% used; 114348618 free inodes.

server4 `/var/tmp`: 105715957760 available bytes; 94.10% used; 114348618 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
