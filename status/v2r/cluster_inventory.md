# V2R cluster inventory

2026-09-24T20:28:00.589852+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 323983458304 available bytes; 81.93% used; 112481437 free inodes.

server1 `/home`: 323983458304 available bytes; 81.93% used; 112481437 free inodes.

server1 `/tmp`: 323983458304 available bytes; 81.93% used; 112481437 free inodes.

server1 `/var/tmp`: 323983458304 available bytes; 81.93% used; 112481437 free inodes.

server1 `/mnt/raid5`: 415626108928 available bytes; 98.09% used; 337634691 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 30159548416 available bytes; 98.32% used; 110411377 free inodes.

server2 `/home`: 30159548416 available bytes; 98.32% used; 110411377 free inodes.

server2 `/tmp`: 30159548416 available bytes; 98.32% used; 110411377 free inodes.

server2 `/var/tmp`: 30159548416 available bytes; 98.32% used; 110411377 free inodes.

server2 `/mnt/raid5`: 492342448128 available bytes; 96.60% used; 445156627 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84395188224 available bytes; 95.29% used; 114156102 free inodes.

server3 `/home`: 84395188224 available bytes; 95.29% used; 114156102 free inodes.

server3 `/data`: 151508451328 available bytes; 97.91% used; 225804436 free inodes.

server3 `/tmp`: 84395188224 available bytes; 95.29% used; 114156102 free inodes.

server3 `/var/tmp`: 84395188224 available bytes; 95.29% used; 114156102 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105640493056 available bytes; 94.10% used; 114348391 free inodes.

server4 `/home`: 105640493056 available bytes; 94.10% used; 114348391 free inodes.

server4 `/data`: 85484249088 available bytes; 98.82% used; 225257963 free inodes.

server4 `/tmp`: 105640493056 available bytes; 94.10% used; 114348391 free inodes.

server4 `/var/tmp`: 105640493056 available bytes; 94.10% used; 114348391 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
