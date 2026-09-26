# V2R cluster inventory

2026-09-26T08:58:04.870940+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318745116672 available bytes; 82.22% used; 112475806 free inodes.

server1 `/home`: 318745116672 available bytes; 82.22% used; 112475806 free inodes.

server1 `/tmp`: 318745116672 available bytes; 82.22% used; 112475806 free inodes.

server1 `/var/tmp`: 318745116672 available bytes; 82.22% used; 112475806 free inodes.

server1 `/mnt/raid5`: 219037106176 available bytes; 99.00% used; 337538800 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22316519424 available bytes; 98.76% used; 110403907 free inodes.

server2 `/home`: 22316519424 available bytes; 98.76% used; 110403907 free inodes.

server2 `/tmp`: 22316519424 available bytes; 98.76% used; 110403907 free inodes.

server2 `/var/tmp`: 22316519424 available bytes; 98.76% used; 110403907 free inodes.

server2 `/mnt/raid5`: 255150141440 available bytes; 98.24% used; 445023943 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82661912576 available bytes; 95.39% used; 114110812 free inodes.

server3 `/home`: 82661912576 available bytes; 95.39% used; 114110812 free inodes.

server3 `/data`: 123663970304 available bytes; 98.29% used; 225828317 free inodes.

server3 `/tmp`: 82661912576 available bytes; 95.39% used; 114110812 free inodes.

server3 `/var/tmp`: 82661912576 available bytes; 95.39% used; 114110812 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106054901760 available bytes; 94.08% used; 114348132 free inodes.

server4 `/home`: 106054901760 available bytes; 94.08% used; 114348132 free inodes.

server4 `/data`: 89348579328 available bytes; 98.77% used; 224883337 free inodes.

server4 `/tmp`: 106054901760 available bytes; 94.08% used; 114348132 free inodes.

server4 `/var/tmp`: 106054901760 available bytes; 94.08% used; 114348132 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
