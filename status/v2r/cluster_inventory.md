# V2R cluster inventory

2026-09-25T19:35:07.363644+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318725701632 available bytes; 82.22% used; 112476326 free inodes.

server1 `/home`: 318725701632 available bytes; 82.22% used; 112476326 free inodes.

server1 `/tmp`: 318725701632 available bytes; 82.22% used; 112476326 free inodes.

server1 `/var/tmp`: 318725701632 available bytes; 82.22% used; 112476326 free inodes.

server1 `/mnt/raid5`: 370854338560 available bytes; 98.30% used; 337540782 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 23095320576 available bytes; 98.71% used; 110407936 free inodes.

server2 `/home`: 23095320576 available bytes; 98.71% used; 110407936 free inodes.

server2 `/tmp`: 23095320576 available bytes; 98.71% used; 110407936 free inodes.

server2 `/var/tmp`: 23095320576 available bytes; 98.71% used; 110407936 free inodes.

server2 `/mnt/raid5`: 311904657408 available bytes; 97.84% used; 445064270 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84381356032 available bytes; 95.29% used; 114152625 free inodes.

server3 `/home`: 84381356032 available bytes; 95.29% used; 114152625 free inodes.

server3 `/data`: 128228745216 available bytes; 98.23% used; 225808487 free inodes.

server3 `/tmp`: 84381356032 available bytes; 95.29% used; 114152625 free inodes.

server3 `/var/tmp`: 84381356032 available bytes; 95.29% used; 114152625 free inodes.
| server4 | True | ['3', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105674612736 available bytes; 94.10% used; 114349578 free inodes.

server4 `/home`: 105674612736 available bytes; 94.10% used; 114349578 free inodes.

server4 `/data`: 229592510464 available bytes; 96.83% used; 224929734 free inodes.

server4 `/tmp`: 105674612736 available bytes; 94.10% used; 114349578 free inodes.

server4 `/var/tmp`: 105674612736 available bytes; 94.10% used; 114349578 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
